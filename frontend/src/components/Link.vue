<template>
    <button @click="router(path)">
        <slot></slot>
    </button>
</template>

<script>
export default {
  name: 'Link',
  props:{
      path:String
  },
  methods:{
    router(path){
      this.$router.push(path)
    }
  }
}
</script>

