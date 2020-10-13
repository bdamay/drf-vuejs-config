<template>
  <div id="test-component">
    <h2>Test component {{ name }}</h2>
    <h3> {{ subname }}</h3>
  </div>
</template>

<script>
  export default {
    name: "Test",
    data: function() {
      return {
        name: 'My component Name ',
        subname: 'My component SubName'
      }
    }
  }
</script>

<style scoped>
  h1 {
    font-color: #cc5d24
  }
</style>
