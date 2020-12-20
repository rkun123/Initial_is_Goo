<template>
  <div class="home">
    <div class="cp_iptxt">
      <input type="text" :placeholder="placeholder" v-model="text">
      <img src="@/assets/enter_3719.png" class="icon" @click="check_room">
    </div>
  </div>
  
</template>

<script>

export default {
  name: 'Home',
  data(){
    return {
      room_id:"",
      text: ""
    }
  },
  methods: {
    check_room(){
      this.$router.push('/user')
    }
  },
  components: {
  },
  props:{
      placeholder: String
  },
  watch: {
    text: function() {
      this.$parent.room = this.text
    }
  }
}
</script>

<style>
.cp_iptxt {
    position: relative;
    width: 40%;
  max-width: 400px;
  margin: auto;
  
}
.cp_iptxt input[type=text] {
	font: 20px/24px sans-serif;
	box-sizing: border-box;
	width: 100%;
  height: 60px;
	margin: auto;
	padding: 0.3em;
	transition: 0.3s;
	border: 1px solid #1b2538;
	border-radius: 4px;
	outline: none;
  border-top-left-radius: 50px;
  border-top-right-radius: 50px;
  border-bottom-right-radius: 50px;
  border-bottom-left-radius: 50px;
}
.cp_iptxt input[type=text]:focus {
	border-color: #da3c41;
}
.cp_iptxt input[type=text] {
	padding-left: 15px;
  padding-right: 35px;
}
.cp_iptxt img {
	position: absolute;
  vertical-align: middle;
  padding-top: 1.3vh;
  padding-right: 7px;
	right: 0;
	transition: 0.3s;
	color: #aaaaaa;
  width: 40px;
  right: 3%;
}
.cp_iptxt input[type=text]:focus + i {
	color: #da3c41;
}

</style>
