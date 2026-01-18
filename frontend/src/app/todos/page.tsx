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
      <div className="min-h-screen bg-black">
        <nav className="bg-dark-light border-b border-primary-900/30 shadow-lg shadow-primary-900/20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex justify-between h-16">
              <div className="flex items-center">
                <div className="flex items-center space-x-3">
                  <div className="w-10 h-10 bg-gradient-to-br from-primary-600 to-primary-500 rounded-xl flex items-center justify-center shadow-lg shadow-primary-500/50">
                    <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                    </svg>
                  </div>
                  <h1 className="text-2xl font-bold gradient-text">
                    My Todos
                  </h1>
                </div>
              </div>
              <div className="flex items-center">
                <button
                  onClick={handleLogout}
                  className="flex items-center space-x-2 text-gray-400 hover:text-red-400 px-4 py-2 rounded-lg hover:bg-red-950/30 transition-all duration-200 font-medium border border-transparent hover:border-red-500/30"
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                  </svg>
                  <span>Logout</span>
                </button>
              </div>
            </div>
          </div>
        </nav>

        <main className="max-w-4xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
          {loading && (
            <div className="text-center py-20">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent"></div>
              <p className="mt-4 text-gray-400 font-medium">Loading your todos...</p>
            </div>
          )}

          {error && (
            <div className="card p-6 bg-red-950/50 border-2 border-red-500 animate-fade-in">
              <div className="flex items-center space-x-3">
                <svg className="w-6 h-6 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <p className="text-red-300 font-medium">{error}</p>
              </div>
            </div>
          )}

          {!loading && !error && (
            <div className="space-y-6">
              <AddTodoForm onAdd={handleAddTodo} />
              <TodoList todos={todos} onToggle={handleToggleTodo} onDelete={handleDeleteTodo} />
            </div>
          )}
        </main>
      </div>
    </ProtectedRoute>
  );
}
