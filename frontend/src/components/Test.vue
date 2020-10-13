<template>
  <div id="test-component">
    <h2>Component Name: {{ name }}</h2>
    <h3> Component subname: {{ subname }}</h3>
    <h4>Play with input validation </h4>
    <input type="text" class='input-lg' v-model="email"/>
    <div class="alert" v-if="!email_valid">La saisie n'est pas un email</div>


    <H4>Test QRCODE component</H4>
    <vue-qrcode :value="qrcode" :options="{ width: 200 }"></vue-qrcode>
  </div>
</template>

<script>

import VueQrcode from '@chenfengyuan/vue-qrcode';
  export default {
    name: "Test",
    components: {VueQrcode},
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
      qrcode () {
        return this.email ? this.email : 'empty'
      }

    }

  }
</script>

<style scoped>
  .alert {
    font-weight: bold;
    color: #cc1d15
  }
</style>
