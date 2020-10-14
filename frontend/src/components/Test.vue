<template>
  <div id="test-component">
    <h2>Component Name: {{ name }}</h2>
    <h3> Component subname: {{ subname }}</h3>
    <h4>Play with input validation </h4>
    <input type="text" class='input-lg' v-model="email"/>
    <div class="alert" v-if="!email_valid">La saisie n'est pas un email</div>


  </div>
</template>

<script>

  export default {
    name: "Test",
    data () {
      return {
        name: 'My component Name ',
        subname: 'My component SubName',
        email: ''
      }
    },
    computed: {
      email_valid () {
        return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(this.email)
      },

    }

  }
</script>

<style scoped>
  .alert {
    font-weight: bold;
    color: #cc1d15
  }
</style>
