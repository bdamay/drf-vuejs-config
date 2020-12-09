<template>
  <v-app>
    <v-app-bar>tatat</v-app-bar>
    <h1> {{ msg }} </h1>
    <test></test>

  </v-app>
</template>

<script>
   import Test from './components/Test.vue'
    export default {
        name: 'app',
        components:{Test},
        data () {
            return {
                msg: 'Bienvenue sur un VueJS app main avec hot reload ',
            }
        },
    }
</script>

<style lang="scss">
  #app {
    border: 1px solid black;
    padding: 5pt;
  }
</style>
