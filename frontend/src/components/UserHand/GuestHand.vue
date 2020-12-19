<template>
  <div class="guest">
    <img class="win" :src="handname" v-if="!is_win">
    <img class="lose" :src="handname" v-if="is_win">
    <p>{{username}}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      handname:""
    }
  },
  props: {
    hand:String,
    username:String,
    is_win:Boolean
  },
  mounted: function() {
    this.handname = "/hands/"+this.hand+".png"
  },
  watch: {
    hand: function() {
      this.handname = "/hands/"+this.hand+".png"
    }
  }
}
</script>

<style scoped>
.guest{
  background-color: whitesmoke;
  border: solid;
  border-radius: 10px;
  width: 200px;
  height: 250px;
}
.win{
  margin-top: 10px;
  height: 150px;
}
.lose{
  margin-top: 10px;
  height: 150px;
  filter:grayscale(100%);
}
.guest p {
  margin-top: 10px;
  font-size: 30px;
}
</style>
