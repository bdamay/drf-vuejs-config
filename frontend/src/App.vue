<template>
  <div>
    <h1> {{ msg }} </h1>
    <qr-code-test></qr-code-test>

  </div>
</template>

<script>
   import Test from './components/Test.vue'
   import QrCodeTest from "./components/QrCodeTest";
    export default {
        name: 'app',
        components:{QrCodeTest, Test},
        data () {
            return {
                msg: 'Application VueJS avec hot reload ',
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
