<template>
  <div class="guest">
    <img :src="handname">
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
    username:String
  },
  mounted: function() {
    this.handname = "/hands/"+this.hand+".png"
  },
  watch: {
    hand: function() {
      this.handname = "/hands/"+this.hand+".png"
      console.log(this.handname)
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
img{
  margin-top: 10px;
  height: 150px;
}
.guest p {
  margin-top: 10px;
  font-size:calc(2rem + ((1vw - 0.5rem) * 4));
}
</style>
