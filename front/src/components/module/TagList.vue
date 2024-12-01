<script setup lang="ts">
import type { Tag } from '@/utils/api/services/tags/tags.type';
interface Props {
  tags: Tag[];
  next: string | null;
}
const props = defineProps<Props>()

const emit = defineEmits<{
    (e: 'tagsPush'): void
}>()

</script>



<template>
    <div class="tags">
        <p class="tag" v-for="tag in props.tags" :key="tag.id">{{ tag.name }}</p>
        <p class="tag" v-if="props.next" @click="emit('tagsPush')">Еще...</p>
    </div>
</template>

<style scoped>

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
  flex-direction: row;
  padding: 16px;
}

.tag {
  padding: 5px 10px;
  border-radius: 30px;
  background-color: var(--secondary);
  color: var(--white);
  
}
.tag:hover {
  cursor: pointer;
  background-color: var(--quinary);
}
.tag:active {
  background-color: var(--quinary);
}
</style>