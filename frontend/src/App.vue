<template>

  <v-app>
    <v-navigation-drawer
            v-model="drawer"
            app
    >
    </v-navigation-drawer>

    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-app-bar>

    <v-main app>
      <v-container fluid height="100vh">
        <v-flex class="flex-row" height="100%">
          <v-row>
            <v-col cols="12">
              <v-card height="200">
                Test Icon
                <v-icon>mdi-arrow-collapse-down</v-icon>
                <h1> {{ msg }} </h1>
              </v-card>
            </v-col>
          </v-row>
          <test class="flex-grow-1"></test>
        </v-flex>
      </v-container>

    </v-main>
    <v-footer app class="text-right"> cool footer</v-footer>
  </v-app>
</template>

<script>
  import Test from './components/Test.vue'
  export default {
    name: 'app',
    components:{Test},
    data () {
      return {
        msg: 'VueJS vuetify django integration ',
        drawer: null
      }
    },
  }
</script>

<style >

</style>
