<script setup lang="ts">
import type { Master } from '@/utils/api/services/masters/masters.type'
import { ref } from 'vue';
import TagList from '@/components/module/TagList.vue';

defineProps<{
  master: Master
}>()
const showDetail = ref(false)


const showDetailHandler = () => {
  showDetail.value = !showDetail.value
}


</script>

<template>
  <div class="master-card" @mouseenter="showDetailHandler" @mouseleave="showDetailHandler">
    <div class="master-image">
      <img :src="master.image" :alt="master.name" v-if="master.image">
      <div class="no-photo" v-else>Нет фото</div>
    </div>
    <TagList :tags="master.tags.slice(0, 5)" :next="null" @tagsPush="null" />
    <div class="master-info">
      <p class="master-cost">{{ master.start_cost }}</p>
      <h3 class="master-name">{{ master.name }}</h3>
    </div>
    <div class="master-detail" v-if="showDetail">
      <div class="detail-content des-l" >
        <p>{{ master.short_description || 'Мастер еще не добавил свое описание 😢' }}</p>
        <div class="master-sub-info">
          <p>Опыт: {{ master.experience }} Года</p>
          <div class="rating">Рейтинг: {{ master.rating }} ⭐</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.master-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  width: 400px;
  margin: 0 auto;
  margin-bottom: 20px;
}

.master-card:hover {
  transform: translateY(-4px);
  transition: transform 0.2s ease-in-out;
}

.master-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
  background: #f5f5f5;
}

.master-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.no-photo {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #666;
}

.master-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 16px;
}

.master-cost {
  margin: 0 0 8px;
  font-size: 1.2em;
  color: #333;
  transition: transform 0.2s ease-in-out, text-decoration 0.2s ease-in-out;
}

.master-cost::before {
  content: 'от ';
}

.master-cost::after {
  content: ' ₽';
}

.master-cost:hover {
  transform: scale(1.1);
  text-decoration: underline;

}

.master-name {  
  margin: 0 0 8px;
  font-size: 1.2em;
  color: #333;
}

.master-detail {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: start;
  justify-content: space-around;
  padding: 20px;
  color: var(--white);
  opacity: 0;
  transition: opacity 0.2s ease-in-out;
}

.master-card:hover .master-detail {
  opacity: 1;
}

.master-detail-content {
  padding: 16px;
  max-width: 80%;
  text-align: center;

}

.master-sub-info {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 10px;
}
</style>