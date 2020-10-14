<template>
  <div id="test-component">
    <h2>Test QR - Code </h2>
    <h3> Component subname: {{ subname }}</h3>
    <h4>input qrcode value </h4>
    <input type="text" class='input-lg' v-model="qrcode"/>
    <H4>QRCode</H4>
    <vue-qrcode :value="qrcode" :options="{ width: 200 }"></vue-qrcode>
  </div>
</template>

<script>

import VueQrcode from '@chenfengyuan/vue-qrcode';
import { QrcodeStream, QrcodeDropZone, QrcodeCapture } from 'vue-qrcode-reader'

  export default {
    name: "QrCodeTest",
    components: {VueQrcode, QrcodeStream, QrcodeDropZone, QrcodeCapture},
    data () {
      return {
        qrcode: ''
      }
    },
    computed: {

    }

  }
</script>

<style scoped>
  .alert {
    font-weight: bold;
    color: #cc1d15
  }
</style>
