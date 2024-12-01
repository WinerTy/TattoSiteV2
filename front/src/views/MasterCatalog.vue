<script setup lang="ts">
import { onMounted, watch } from 'vue'
import { useMastersStore } from '@/stores/masters.store'
import { useSalonStore } from '@/stores/salon.store'
import MasterCard from '@/components/module/MasterCard.vue'
import LoadingIndicator from '@/components/shared/LoadingIndicator.vue'
import PaginationLine from '@/components/shared/PaginationLine.vue'
import TagList from '@/components/module/TagList.vue'
import { useTagsStore } from '@/stores/tags.store'

const mastersStore = useMastersStore()
const salonStore = useSalonStore()
const tagsStore = useTagsStore()

onMounted(async () => {
  await mastersStore.fetchMasters()
  await tagsStore.fetchTags()
})


watch(
  () => salonStore.selectedSalonId,
  async (newSalonId) => {
    if (newSalonId) {
      mastersStore.reset()
      tagsStore.reset()
      await mastersStore.fetchMasters()
      await tagsStore.fetchTags()
    }
  }
)
</script>

<template>
  <div class="masters">
    <div class="master-header">
      <h1>Наши мастера</h1>
      <p v-if="mastersStore.count > 0">Найдено: {{ mastersStore.count }}</p>
    </div>
    <div class="list-chips">
      <TagList :tags="tagsStore.tags" :next="tagsStore.next" @tagsPush="tagsStore.tagsPush"/>
    </div>
    <div v-if="!salonStore.selectedSalonId" class="no-salon-message">
      Пожалуйста, выберите салон
    </div>
    
    <div v-else-if="mastersStore.loading" class="loading">
      <LoadingIndicator message="Загрузка мастеров..." />
    </div>

    <div v-else-if="mastersStore.error" class="error-message">
      {{ mastersStore.error }}
    </div>
    
    <div v-else-if="!mastersStore.hasMasters" class="no-masters-message">
      <p class="des">В данном салоне пока нет мастеров</p>
    </div>
    <div v-else class="masters-grid">
      <MasterCard
        v-for="master in mastersStore.getAllMasters"
        :key="master.id"
        :master="master"
      />
    </div>
    <PaginationLine
      v-if="mastersStore.total_pages > 1"
      :currentPage="mastersStore.currentPage"
      :totalPages="mastersStore.total_pages"
      @prevPage="mastersStore.prevPage"
      @nextPage="mastersStore.nextPage"
      @changePage="mastersStore.changePage"
    />
  </div>

</template>

<style scoped>
.master-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  padding: 20px;
  width: 100%;
}

.list-chips{
  display: flex;
  justify-content: start;
  width: 100%;
}
.masters-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  grid-auto-rows: minmax(100px, auto);
  margin-top: 20px;
}

.masters {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.loading,
.error-message,
.no-salon-message,
.no-masters-message {
  text-align: center;
  padding: 20px;
  margin: 20px 0;
  border-radius: 8px;
  background-color: rgb(30, 32, 33);;
}

.error-message {
  color: #dc3545;
  background-color: #f8d7da;
}
</style>