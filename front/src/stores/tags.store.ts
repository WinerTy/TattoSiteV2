import { defineStore } from 'pinia'
import { api } from '@/utils/api'
import { useSalonStore } from './salon.store'
import type { Tag, TagParams } from '@/utils/api/services/tags/tags.type'
import type { ApiResponse } from '@/utils/api/base/base.type'

interface TagsState {
  tags: Tag[]
  count: number
  currentPage: number
  prev: string | null
  next: string | null
  total_pages: number
  loading: boolean
  error: string | null
}

export const useTagsStore = defineStore('tags', {
  state: (): TagsState => ({
    tags: [],
    count: 0,
    currentPage: 1,
    prev: null,
    next: null,
    total_pages: 1,
    loading: false,
    error: null,
  }),
  actions: {
    async fetchTags() {
      const salonStore = useSalonStore()
      if (!salonStore.selectedSalonId) {
        this.setError('Салон не выбран')
        return
      }
      this.loading = true
      this.error = null
      try {
        const params: TagParams = { salon_id: salonStore.selectedSalonId, page: this.currentPage }
        const response = await api.tags.getTags(params)
        this.setTags(response.data)
      } catch (error) {
        this.setError(
          error instanceof Error ? error.message : 'Произошла ошибка при загрузке тегов',
        )
      } finally {
        this.loading = false
      }
    },
    reset() {
      this.tags = []
      this.count = 0
      this.next = null
      this.prev = null
      this.error = null
      this.loading = false
      this.total_pages = 1
      this.currentPage = 1
    },
    async tagsPush() {
      if (this.next) {
        this.loading = true
        this.error = null
        try {
          const salonStore = useSalonStore()
          if (!salonStore.selectedSalonId) {
            this.setError('Салон не выбран')
            return
          }
          const params: TagParams = {
            salon_id: salonStore.selectedSalonId,
            page: ++this.currentPage,
          }
          const response = await api.tags.getTags(params)
          this.addTags(response.data)
        } catch (error) {
          this.setError(
            error instanceof Error ? error.message : 'Произошла ошибка при загрузке тегов',
          )
        } finally {
          this.loading = false
        }
      }
    },

    addTags(data: ApiResponse<Tag>) {
      this.tags.push(...data.results)
      this.count = data.count
      this.next = data.next
      this.prev = data.previous
      this.total_pages = data.total_pages
    },

    setTags(data: ApiResponse<Tag>) {
      this.tags = data.results
      this.count = data.count
      this.next = data.next
      this.prev = data.previous
      this.total_pages = data.total_pages
    },

    setError(error: string) {
      this.error = error
    },
  },
})
