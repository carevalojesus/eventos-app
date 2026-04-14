/**
 * 🔌 Cliente API — centraliza todas las llamadas al backend Django.
 *
 * 🎯 Puntos didácticos:
 *   • Usamos fetch nativo del navegador (no necesitamos axios).
 *   • La URL base se lee de variable de entorno PUBLIC_API_URL.
 *   • Cada función retorna una Promise con los datos parseados como JSON.
 *   • Manejamos errores HTTP lanzando excepciones descriptivas.
 */

const API = import.meta.env.PUBLIC_API_URL || 'http://localhost:8000/api';

/** Helper interno: lanza error si la respuesta no es 2xx */
async function handle(res) {
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`HTTP ${res.status}: ${detail}`);
  }
  // 204 No Content (típico en DELETE)
  if (res.status === 204) return null;
  return res.json();
}

// 📋 Listar todos los eventos
export async function listarEventos() {
  const res = await fetch(`${API}/eventos/`);
  return handle(res);
}

// 🔍 Obtener un evento por ID
export async function obtenerEvento(id) {
  const res = await fetch(`${API}/eventos/${id}/`);
  return handle(res);
}

// ➕ Crear un evento nuevo
export async function crearEvento(data) {
  const res = await fetch(`${API}/eventos/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return handle(res);
}

// ✏️ Actualizar un evento (parcial)
export async function actualizarEvento(id, data) {
  const res = await fetch(`${API}/eventos/${id}/`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return handle(res);
}

// 🗑️ Eliminar un evento
export async function eliminarEvento(id) {
  const res = await fetch(`${API}/eventos/${id}/`, { method: 'DELETE' });
  return handle(res);
}

// 🔄 Alternar estado activo/inactivo (acción personalizada)
export async function toggleEvento(id) {
  const res = await fetch(`${API}/eventos/${id}/toggle/`, { method: 'POST' });
  return handle(res);
}
