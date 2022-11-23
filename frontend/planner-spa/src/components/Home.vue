<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Recentes Cards</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card" v-for="planner in planners" v-bind:key="planner.id">
          <div class="card-content">
            <p class="title">{{ planner.name}}</p>
            <p class='subtitle'>{{ planner.created_at }}</p>
          </div>
          <div class="card-foooter">
            <router-link :to="`planners/${planner.id}`" class="card-footer-item">Ver Planner</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: mapState({
    planners: state => state.planners
  }),
  beforeMount () {
    this.$store.dispatch('loadPlanners')
  }
}
</script>

<style>

</style>
