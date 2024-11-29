<script setup lang="ts">
import { useSalonStore } from '@/stores/salon.store';
import { onMounted } from 'vue';

const salonStore = useSalonStore()

onMounted(() => {
  salonStore.fetchSalons()
})

function selectSalon(event: Event) {
  const target = event.target as HTMLSelectElement
  salonStore.selectSalon(Number(target.value))
}


</script>

<template>
  <select 
    :value="salonStore.selectedSalon?.id"
    @change="selectSalon" 
    class="select des-l nav-size p-5-10"
  >
    <option v-for="salon in salonStore.salons" :key="salon.id" :value="salon.id" class="des-l nav-size">
      {{ salon.name }}
    </option>
  </select>
</template>

<style scoped>

.select {
  border-radius: 5px;
  background-color: var(--secondary);
  color: var(--white);
  border: none;
  cursor: pointer;
}

</style>