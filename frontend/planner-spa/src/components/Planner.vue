<template>
    <div>
      <!-- omitted for brevity -->
      <section class="section">
        <div class="container">
  
          <div class="columns">
            <div class="column is-10 is-offset-1">
  
              <div v-for="(card, idx) in planner.cards"
                v-bind:key="card.id"
                v-show="currentCard === idx"> 

                    <div class="column is-offset-3 is-6">
                      <h4 class='title has-text-centered'>{{ card.text }}</h4>
                    </div>
                    <div class="column is-offset-4 is-4">
                      <div class="control">
                        <div v-for="task in card.tasks" v-bind:key="task.id">
                          <label class="radio">
                          <input type="radio" v-model="card.task" :value="task.id">
                          {{ task.text }}
                          </label>
                        </div>
                      </div>
                    </div>
  
              </div>
              
              <div class="column is-offset-one-quarter is-half">
                <nav class="pagination is-centered" role="navigation" aria-label="pagination">
                  <a class="pagination-previous" @click.stop="goToPreviousCard"><i class="fa fa-chevron-left" aria-hidden="true"></i> &nbsp;&nbsp; Voltar</a>
                  <a class="pagination-next" @click.stop="goToNextCard">Avançar &nbsp;&nbsp; <i class="fa fa-chevron-right" aria-hidden="true"></i></a>
                </nav>
              </div>
  
              <!-- new submit button -->
              <div class="column has-text-centered">
                <a v-if="plannerComplete" class='button is-focused is-primary is-large'
                  @click.stop="handleSubmit">
                  Confirmar
                </a>
              </div>
  
            </div>
          </div>
  
        </div>
      </section>
    </div>
</template>

<script>

export default {
    data() {
        return {
            currentCard: 0
        }
    },
    methods: { // new Vue obj member
        goToNextCard() {
            if (this.currentCard === (this.planner.cards.length - 1)) {
                this.currentCard = 0
            } else {
                this.currentCard++
            }
        },
        goToPreviousCard() {
            if (this.currentCard === 0) {
                this.currentCard = this.planner.cards.length - 1
            } else {
                this.currentCard--
            }
        },
        handleSubmit() {
          this.$store.dispatch('addPlannerResponse')
          .then(() => this.$router.push('/'))
        }
    },
    computed: {  // new Vue obj member
        plannerComplete() {
            if (this.planner.cards) {
                const numCards = this.planner.cards.length
                const numCompleted = this.planner.cards.filter(q => q.tasks).length
                return numCards === numCompleted
            }        
        },
        planner() {
            return this.$store.state.currentPlanner
        },
        selectedTask: {
          get() {
            const card = this.planner.cards[this.currentCard]
            return card.tasks
          },
          set(value) {
            const card = this.survey.cards[this.currentCard]
            this.$store.commit('setTask', { cardId: card.id, tasks: value })
          }
        },
        beforeMount: () => {
          this.$store.dispatch('loadPlanner', { id: parseInt(this.$route.params.id) })
        }
    }
    }
</script>