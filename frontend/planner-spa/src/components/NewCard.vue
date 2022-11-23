<template>
    <div>
        <div class="field">
            <label class="label is-large">Card</label>
            <div class="control">
                <input type="text" class="input is-large" v-model="card">
            </div>
        </div>

        <div class="field">
            <div class="control">
                <a class="button is-large is-info" @click="addTask">
                    <span class="icon is-small">
                    <i class="fa fa-plus-square-o fa-align-left" aria-hidden="true"></i>
                    </span>
                    <span>+ Tarefa</span>
                </a>
                <a class="button is-large is-primary" @click="saveCard">
                    <span class="icon is-small">
                        <i class="fa fa-check"></i>
                    </span>
                    <span>Salvar</span>
                </a>
            </div>
        </div>

        <h2 class="label is-large" v-show="tasks.length > 0">Tarefas</h2>
        <div class="field has-addons" v-for="(task, idx) in tasks" v-bind:key="idx">
            <div class="control task">
            <input type="text" class="input is-large" v-model="tasks[idx]">
            </div>
            <div class="control">
            <a class="button is-large">
                <span class="icon is-small" @click.stop="removeTask(task)">
                <i class="fa fa-times" aria-hidden="true">X</i>
                </span>
            </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
    return {
        card: '',
        tasks: []
    }
    },
    methods: {
    removeTask(task) {
        const idx = this.tasks.findIndex(c => c === task)
        this.tasks.splice(idx, 1)
    },
    saveCard() {
        this.$emit('cardComplete', {
        card: this.card,
        tasks: this.tasks.filter(c => !!c)
        })
        this.card = ''
        this.tasks = []
    },
    addTask() {
        this.tasks.push('')
    }
    }
}
</script>

<style>
.task {
    width: 90%;
}
</style>