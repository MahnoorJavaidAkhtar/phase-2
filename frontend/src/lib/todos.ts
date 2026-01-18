/**
 * Todo API functions.
 */

import { apiClient } from './api-client';
import { Todo, TodoCreate } from '@/types';

/**
 * Get all todos for the authenticated user.
 */
export async function getTodos(token: string): Promise<Todo[]> {
  return apiClient.get<Todo[]>('/api/todos', token);
}

/**
 * Create a new todo.
 */
export async function createTodo(data: TodoCreate, token: string): Promise<Todo> {
  return apiClient.post<Todo>('/api/todos', data, token);
}

/**
 * Update an existing todo.
 */
export async function updateTodo(id: number, data: Partial<TodoCreate>, token: string): Promise<Todo> {
  return apiClient.put<Todo>(`/api/todos/${id}`, data, token);
}

/**
 * Delete a todo.
 */
export async function deleteTodo(id: number, token: string): Promise<void> {
  return apiClient.delete<void>(`/api/todos/${id}`, token);
}

/**
 * Toggle todo completion status.
 */
export async function toggleTodoComplete(id: number, isComplete: boolean, token: string): Promise<Todo> {
  return apiClient.patch<Todo>(`/api/todos/${id}`, { is_complete: isComplete }, token);
}
