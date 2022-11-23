import axios from 'axios'

const API_URL = 'http://127.0.0.1:5000/api'

export function fetchPlanner (plannerId) {
  return axios.get(`${API_URL}/planners/${plannerId}/`)
}

export function fetchPlanners () {
  return axios.get(`${API_URL}/planners/`)
}

export function savePlannerResponse (plannerResponse) {
  return axios.put(`${API_URL}/planners/${plannerResponse.id}/`, plannerResponse)
}

export function postNewPlanner (planner, jwt) {
  return axios.post(`${API_URL}/planners/`, planner, { headers: { Authorization: `Bearer: ${jwt}` } })
}

export function authenticate (userData) {
  return axios.post(`${API_URL}/login/`, userData)
}

export function register (userData) {
  return axios.post(`${API_URL}/register/`, userData)
}