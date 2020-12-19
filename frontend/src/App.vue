<template>
  <div id="app">
    <my-header></my-header>
    <div id="nav">
    </div>
    <router-view/>
  </div>
</template>
<script>
import Header from './components/Header' 
export default {
  components: {
    "my-header":Header
  }
}
</script>
<style>
body {
  background: url(/back_img/haikei-plesio.png);
  backdrop-filter: blur(1px)
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
