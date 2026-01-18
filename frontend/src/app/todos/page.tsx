'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import ProtectedRoute from '@/components/auth/ProtectedRoute';
import TodoList from '@/components/todos/TodoList';
import AddTodoForm from '@/components/todos/AddTodoForm';
import { getTodos, createTodo, toggleTodoComplete, deleteTodo } from '@/lib/todos';
import { logout } from '@/lib/auth';
import { Todo } from '@/types';

export default function TodosPage() {
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const token = localStorage.getItem('access_token');
        if (!token) {
          router.push('/signin');
          return;
        }

        const data = await getTodos(token);
        setTodos(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load todos');
      } finally {
        setLoading(false);
      }
    };

    fetchTodos();
  }, [router]);

  const handleAddTodo = async (title: string, description: string) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      router.push('/signin');
      return;
    }

    const newTodo = await createTodo({ title, description }, token);
    setTodos([newTodo, ...todos]);
  };

  const handleToggleTodo = async (id: number, isComplete: boolean) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      router.push('/signin');
      return;
    }

    const updatedTodo = await toggleTodoComplete(id, isComplete, token);
    setTodos(todos.map(todo => todo.id === id ? updatedTodo : todo));
  };

  const handleDeleteTodo = async (id: number) => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      router.push('/signin');
      return;
    }

    await deleteTodo(id, token);
    setTodos(todos.filter(todo => todo.id !== id));
  };

  const handleLogout = async () => {
    try {
      await logout();
      router.push('/signin');
    } catch (err) {
      console.error('Logout failed:', err);
    }
  };

  return (
    <ProtectedRoute>
      <div className="min-h-screen bg-gray-50">
        <nav className="bg-white shadow-sm">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <h1 className="text-xl font-semibold text-gray-900">My Todos</h1>
              </div>
              <div className="flex items-center">
                <button
                  onClick={handleLogout}
                  className="text-gray-700 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium"
                >
                  Logout
                </button>
              </div>
            </div>
          </div>
        </nav>

        <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <div className="px-4 py-6 sm:px-0">
            {loading && (
              <div className="text-center py-12">
                <div className="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900"></div>
                <p className="mt-2 text-gray-600">Loading todos...</p>
              </div>
            )}

            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
                {error}
              </div>
            )}

            {!loading && !error && (
              <>
                <AddTodoForm onAdd={handleAddTodo} />
                <TodoList todos={todos} onToggle={handleToggleTodo} onDelete={handleDeleteTodo} />
              </>
            )}
          </div>
        </main>
      </div>
    </ProtectedRoute>
  );
}
