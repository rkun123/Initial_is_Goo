<template>
  <div id="app">
    <my-header></my-header>
    <div id="nav">
    </div>
    <router-view/>
    <my-footer></my-footer>
  </div>
</template>
<script>
import Header from './components/Header' 
import Footer from './components/Footer'
export default {
  components: {
    "my-header":Header,
    "my-footer":Footer
  }
}
</script>
<style>
body {
  background: url(/back_img/haikei-plesio.png);
  backdrop-filter: blur(1px)
}
#app {
  font-family: 'Noto Sans JP', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-bottom: 500px;
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
