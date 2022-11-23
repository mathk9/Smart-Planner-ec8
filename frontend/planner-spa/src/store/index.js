import Vue from 'vue'
import Vuex from 'vuex'

import { fetchPlanners, fetchPlanner, savePlannerResponse, postNewPlanner, authenticate, register } from '@/api'
import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex)

  const state = {
    // single source of data
    planners: [],
    currentPlanner: {},
    user: {},
    jwt: ''
  }

  const actions = {
    // asynchronous operations
    loadPlanners (context) {
      return fetchPlanners().then((response) => context.commit('setPlanners', { planners: response.data }))
    },
    loadPlanner (context, { id }) {
      return fetchPlanner(id).then((response) => context.commit('setPlanner', { planner: response.data }))
    },
    addPlannerResponse (context) {
      return savePlannerResponse(context.state.currentPlanner)
    },
    submitNewPlanner (context, planner) {
      return postNewPlanner(planner, context.state.jwt.token)
    },
    login (context, userData) {
      context.commit('setUserData', { userData })
      return authenticate(userData)
        .then(response => context.commit('setJwtToken', { jwt: response.data }))
        .catch(error => {
          console.log('Error Authenticating: ', error)
          EventBus.$emit('failedAuthentication', error)
        })
    },
    register (context, userData) {
      context.commit('setUserData', { userData })
      return register(userData)
        .then(context.dispatch('login', userData))
        .catch(error => {
          console.log('Error Registering: ', error)
          EventBus.$emit('failedRegistering: ', error)
        })
    }
  }

  const mutations = {
    // isolated data mutations
    setPlanners (state, payload) {
      state.planners = payload.planners
    },
    setPlanner (state, payload) {
      const nCards = payload.planner.cards.length
      for (let i = 0; i < nCards; i++) {
        payload.planner.cards[i].tasks = null
      }
      state.currentPlanner = payload.planner
    },
    setTask (state, payload) {
      const { cardId, tasks } = payload
      const nCards = state.currentPlanner.cards.length
      for (let i = 0; i < nCards; i++) {
        if (state.currentPlanner.cards[i].id === cardId) {
          state.currentPlanner.cards[i].tasks = tasks
          break
        }
      }
    },
    setUserData (state, payload) {
      console.log('setUserData payload = ', payload)
      state.userData = payload.userData
    },
    setJwtToken (state, payload) {
      console.log('setJwtToken payload = ', payload)
      localStorage.token = payload.jwt.token
      state.jwt = payload.jwt
    }
  }

  const getters = {
    // reusable data accessors
    isAuthenticated (state) {
      return isValidJwt(state.jwt.token)
    }
  }

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store
