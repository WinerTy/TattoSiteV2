<script setup lang="ts">
import { onMounted } from 'vue';
import { useSliderStore } from '@/stores/slider.store';

const sliderStore = useSliderStore()

onMounted(() => {
    sliderStore.fetchSlider()
})
</script>



<template>
    <h1>SLIDER</h1>
</template>



<style scoped>

</style>