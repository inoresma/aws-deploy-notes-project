import axios from 'axios'

// URL de la API de Django apuntando a la instancia de EC2 donde esta alojado el backend
const API_BASE_URL = 'http://34.205.48.219:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const notesApi = {
  getNotes() {
    return api.get('/notes/')
  },

  getNote(id) {
    return api.get(`/notes/${id}/`)
  },

  createNote(noteData) {
    return api.post('/notes/', noteData)
  },

  updateNote(id, noteData) {
    return api.put(`/notes/${id}/`, noteData)
  },

  deleteNote(id) {
    return api.delete(`/notes/${id}/`)
  },

  getImportantNotes() {
    return api.get('/notes/important/')
  }
} 