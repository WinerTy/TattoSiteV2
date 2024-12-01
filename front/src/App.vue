<script setup lang="ts">


import HeaderComponent from './components/global/HeaderComponent.vue';

</script>

<template>
  <HeaderComponent />
  <div class="main">

    <RouterView />
  </div>
</template>



<style scoped>
.main {
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 20px;
  min-height: 100vh;
}
</style>