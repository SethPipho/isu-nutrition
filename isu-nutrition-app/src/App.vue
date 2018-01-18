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
  @import './assets/style/milligram.min.css';
  @import 'http://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic';

  body{
     font-size: 1.2em;
  }

  hr{
    margin-top: 10px;
    margin-bottom:10px;
  }

</style>
