<script setup lang="ts">
defineProps<{
  message?: string
}>()
</script>


<template>
  <div class="loading-container">
    <p v-if="message">{{ message }}</p>
    <div class="loader">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
    </div>
  </div>
</template>


<style scoped>

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.loader {
  display: flex;
  justify-content: center;
  align-items: center;
}

.line {
  width: 10px;
  height: 50px;
  background-color: var(--tertiary);
  margin: 0 5px;
  animation: stretch 1.2s infinite ease-in-out;
}

.line:nth-child(2) {
  animation-delay: -1.1s;
}

.line:nth-child(3) {
  animation-delay: -1s;
}

.line:nth-child(4) {
  animation-delay: -0.9s;
}

.line:nth-child(5) {
  animation-delay: -0.8s;
}

@keyframes stretch {
  0%, 40%, 100% {
    transform: scaleY(0.4);
  }
  20% {
    transform: scaleY(1);
  }
}
</style>