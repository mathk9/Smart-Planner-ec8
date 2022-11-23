<template>
    <div>
      <section class="hero is-primary">
        <div class="hero-body">
          <div class="container has-text-centered">
            <h2 class="title">{{ name }}</h2>
          </div>
        </div>
      </section>
  
      <section class="section">
        <div class="container">
          <div class="tabs is-centered is-fullwidth is-large">
              <ul>
                  <li :class="{'is-active': step == 'name'}" @click="step = 'name'">
                      <a>Nome</a>
                  </li>
                  <li :class="{'is-active': step == 'cards'}" @click="step = 'cards'">
                      <a>Cards</a>
                  </li>
                  <li :class="{'is-active': step == 'review'}" @click="step = 'review'">
                      <a>Ver</a>
                  </li>
              </ul>
          </div>
          <div class="columns">
            <div class="column is-half is-offset-one-quarter">
  
                <div class="name" v-show="step === 'name'">
                    <div class="field">
                        <label class="label" for="name">Planner Nome:</label>
                        <div class="control">
                        <input type="text" class="input is-large" id="name" v-model="name">
                        </div>
                    </div>
                </div>

                <div class="cards" v-show="step === 'cards'">
                    <new-card v-on:cardComplete="appendCard"/>
                </div>

                <div class="review" v-show="step === 'review'">
                <ul>
                    <li class="card" v-for="(card, qIdx) in cards" :key="`card-${qIdx}`">
                    <div class="title">
                        {{ card.card }}
                        <span class="icon is-medium is-pulled-right delete-card"
                        @click.stop="removeQuestion(card)">
                        <i class="fa fa-times" aria-hidden="true"></i>
                        </span>
                    </div>
                    <ul>
                        <li v-for="(task , cIdx) in card.tasks" :key="`task-${cIdx}`">
                        {{ cIdx + 1 }}. {{ task }}
                        </li>
                    </ul>
                    </li>
                </ul>
                <br>
                <div class="control">
                    <a class="button is-large is-primary" @click="submitPlanner">Confirmar</a>
                </div>

                </div>
  
            </div>
          </div>
        </div>
      </section>
    </div>
</template>

<script>
import NewCard from '@/components/NewCard'

export default {
    components: { NewCard },
    data() {
        return {
            step: 'name',
            name: '',
            cards: []
        }
    },
    methods: {
        appendCard(newCard) {
            this.cards.push(newCard)
        },
        removeCard(card) {
            const idx = this.cards.findIndex(q => q.card === card.card)
            this.cards.splice(idx, 1)
        },
        submitPlanner() {
            this.$store.dispatch('submitNewPlanner', {
            name: this.name,
            cards: this.cards
        })
            .then(() => this.$router.push('/'))
            .catch((error) => {
            console.log('Error ao criar planner', error)
            this.$router.push('/')
            })
        }
    }
}
</script>

<style></style>