<template>
  <div id="app" class="container">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Hello World'
    }
  }
}
</script>

<style>
  @import './assets/style/bootstrap.min.css'
</style>
