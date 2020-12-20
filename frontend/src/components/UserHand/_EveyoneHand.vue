<template>
  <div>
    <h2>みんなの手</h2>
    <div class="hands_container">
      <div class="everyone" v-for="(hand, number) in hands" :key="number">
        <guest-hand :hand="hand.hand" :username="hand.name" class="guestHand"/>
      </div>
    </div>
  </div>
</template>

<script>
import GuestHand from './GuestHand.vue'

export default {
  data() {
    return{
      hands:[]
    }
  },
  props: {
    _data:[]
  },
  components: {
    GuestHand
  },
  watch:{
    _data: function() {
      this.hands = this._data
      console.log(this.hands)
    }
  },
  mounted: function() {
    this.hands = this._data
      console.log(this.hands)
  }
}
</script>

<style scoped>
.hands_container {
  display: flex;
  flex-wrap :wrap;
}
.everyone .guestHand {
  size: 80%;
  margin: 5px;
}
</style>
