import { api } from '@/utils/api'
import type { Master, MasterParams } from '@/utils/api/services/masters/masters.type'
import { defineStore } from 'pinia'
import { useSalonStore } from './salon.store'
import type { ApiResponse } from '@/utils/api/base/base.type'

interface MastersState {
  masters: Master[]
  count: number
  next: string | null
  prev: string | null
  total_pages: number
  currentPage: number
  loading: boolean
  error: string | null
}

export const useMastersStore = defineStore('masters', {
  state: (): MastersState => ({
    masters: [],
    count: 0,
    next: null,
    prev: null,
    total_pages: 1,
    currentPage: 1,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchMasters() {
      const salonStore = useSalonStore()

      if (!salonStore.selectedSalonId) {
        this.setError('Салон не выбран')
        return
      }

      this.setLoading(true)

      try {
        const params: MasterParams = { salon: salonStore.selectedSalonId, page: this.currentPage }
        const response = await api.master.getMasters(params)
        this.setMasters(response.data)
      } catch (error) {
        this.setError(
          error instanceof Error ? error.message : 'Произошла ошибка при загрузке мастеров',
        )
      } finally {
        this.setLoading(false)
      }
    },

    async changePage(page: number) {
      if (page >= 1 && page <= this.total_pages) {
        this.currentPage = page
        await this.fetchMasters()
      }
    },

    async nextPage() {
      if (this.currentPage < this.total_pages) {
        this.currentPage++
        await this.fetchMasters()
      }
    },

    async prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--
        await this.fetchMasters()
      }
    },

    reset() {
      this.masters = []
      this.count = 0
      this.next = null
      this.prev = null
      this.error = null
      this.loading = false
      this.total_pages = 1
      this.currentPage = 1
    },

    setMasters(data: ApiResponse<Master>) {
      this.masters = data.results
      this.count = data.count
      this.next = data.next
      this.prev = data.previous
      this.total_pages = data.total_pages
    },

    setLoading(loading: boolean) {
      this.loading = loading
    },

    setError(error: string | null) {
      this.error = error
      if (error) {
        this.masters = []
      }
    },
  },

  getters: {
    getAllMasters(): Master[] {
      return this.masters
    },

    hasMasters(): boolean {
      return this.masters.length > 0
    },
  },
})
