import { api } from '@/utils/api'
import type { Salon } from '@/utils/api/services/salon.type'
import { defineStore } from 'pinia'

interface SalonState {
  salons: Salon[]
  loading: boolean
  error: string | null
  selectedSalonId: number | null
}

export const useSalonStore = defineStore('salon', {
  state: (): SalonState => ({
    salons: [],
    loading: false,
    error: null,
    selectedSalonId: Number(localStorage.getItem('selectedSalonId')) || null,
  }),
  actions: {
    async fetchSalons() {
      this.loading = true
      this.error = null

      try {
        this.salons = (await api.salon.getSalons()).data.results
        // Если есть сохраненный ID, но салон еще не загружен
        if (this.selectedSalonId && !this.selectedSalon) {
          const exists = this.salons.some(salon => salon.id === this.selectedSalonId)
          if (!exists) {
            this.selectedSalonId = null
            localStorage.removeItem('selectedSalonId')
          }
        }
      } catch (error) {
        this.error = 'Error fetching salons'
      } finally {
        this.loading = false
      }
    },
    selectSalon(salonId: number) {
      const salon = this.salons.find((salon) => salon.id === salonId)
      if (salon) {
        this.selectedSalonId = salonId
        localStorage.setItem('selectedSalonId', salonId.toString())
      }
    },
  },
  getters: {
    selectedSalon: (state): Salon | null => {
      return state.selectedSalonId 
        ? state.salons.find(salon => salon.id === state.selectedSalonId) || null 
        : null
    }
  }
})
