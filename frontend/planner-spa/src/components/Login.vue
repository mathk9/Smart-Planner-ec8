<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Login ou Cadastro</h2>
          <p class="subtitle error-msg">{{ errorMsg }}</p>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="field">
          <label class="label  is-large" for="email">Email:</label>
          <div class="control">
            <input type="email" class="input is-large" id="email" v-model="email">
          </div>
        </div>
        <div class="field">
          <label class="label  is-large" for="password">Senha:</label>
          <div class="control">
            <input type="password" class="input is-large" id="password" v-model="password">
          </div>
        </div>

        <div class="control">
          <a class="button is-large is-primary" @click="authenticate">Login</a>
          <a class="button is-large is-success" @click="register">Cadastrar</a>
        </div>

      </div>
    </section>

  </div>
</template>

<script>
import { EventBus } from '@/utils'
export default {
  data () {
    return {
      email: '',
      password: '',
      errorMsg: ''
    }
  },
  methods: {
    authenticate () {
      console.log('email: '+ this.email +' password: '+ this.password)
      this.$store.dispatch('login', { email: this.email, password: this.password })
        .then(() => this.$router.push('/'))
    },
    register () {
      this.$store.dispatch('register', { email: this.email, password: this.password })
        .then(() => this.$router.push('/'))
    }
  },
  mounted () {
    EventBus.$on('failedRegistering', (msg) => {
      this.errorMsg = msg
    })
    EventBus.$on('failedAuthentication', (msg) => {
      this.errorMsg = msg
    })
  },
  beforeDestroy () {
    EventBus.$off('failedRegistering')
    EventBus.$off('failedAuthentication')
  }
}
</script>

<style>
.error-msg {
  color: red;
  font-weight: bold;
}
</style>