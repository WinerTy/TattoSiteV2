<script setup lang="ts">
const props = defineProps<{
    currentPage: number,
    totalPages: number
}>()


const emit = defineEmits<{
    (e: 'prevPage'): void
    (e: 'nextPage'): void
    (e: 'changePage', page: number): void
}>()



const prevPage = () => {
    if( props.currentPage > 1 ) {
        emit('prevPage')
    }
}
const nextPage = () => {
    if( props.currentPage < props.totalPages ) {
        emit('nextPage')
    }
}
const changePage = (page: number) => {
    emit('changePage', page)
}
</script>



<template>
    <div class="pagination">
        <div class="prev" :class="{disabled: currentPage === 1}" @click="prevPage">&lt;</div>
        <div class="pagination-item" v-for="page in totalPages" :key="page" @click="changePage(page)" :class="{active: page === currentPage}">{{ page }}</div>
        <div class="next" :class="{disabled: currentPage === totalPages}" @click="nextPage">&gt;</div>
    </div>
</template>



<style scoped>

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.pagination-item, .prev, .next {
  margin: 0 5px;
  cursor: pointer;
  padding: 5px 10px;
  border: 1px solid var(--secondary);
  border-radius: 4px;
  transition: background-color 0.8s ease, color 0.8s ease, border-color 0.8s ease;
}

.pagination-item.active, .pagination-item:hover, .prev:hover, .next:hover {
  background-color: var(--quinary);
  color: white;
  border-color: var(--quinary);
}


.prev.disabled, .next.disabled {
  opacity: 0.5;
  cursor: context-menu;
}

.prev.disabled:hover, .next.disabled:hover {
  background-color: var(--primary);
  color: var(--secondary);
  border-color: var(--secondary);
}
</style>