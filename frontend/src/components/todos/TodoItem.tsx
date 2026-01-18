/**
 * TodoItem component - displays a single todo item with interactive controls.
 */

'use client';

import { Todo } from '@/types';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: number, isComplete: boolean) => Promise<void>;
  onDelete: (id: number) => Promise<void>;
}

export default function TodoItem({ todo, onToggle, onDelete }: TodoItemProps) {
  const handleToggle = async () => {
    await onToggle(todo.id, !todo.is_complete);
  };

  const handleDelete = async () => {
    if (confirm('Are you sure you want to delete this todo?')) {
      await onDelete(todo.id);
    }
  };

  return (
    <div className="card p-5 hover:border-primary-600/50 transition-all duration-300 group">
      <div className="flex items-start justify-between gap-4">
        <div className="flex items-start flex-1 gap-4">
          <div className="flex items-center pt-1">
            <input
              type="checkbox"
              checked={todo.is_complete}
              onChange={handleToggle}
              className="h-5 w-5 text-primary-600 focus:ring-2 focus:ring-primary-500 border-2 border-primary-700 rounded cursor-pointer transition-all bg-dark-lighter"
            />
          </div>
          <div className="flex-1 min-w-0">
            <h3 className={`text-base font-semibold transition-all ${
              todo.is_complete
                ? 'line-through text-gray-500'
                : 'text-white group-hover:text-primary-400'
            }`}>
              {todo.title}
            </h3>
            {todo.description && (
              <p className={`mt-1 text-sm ${
                todo.is_complete ? 'text-gray-600' : 'text-gray-400'
              }`}>
                {todo.description}
              </p>
            )}
            <div className="mt-2 flex items-center gap-2">
              <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                todo.is_complete
                  ? 'bg-primary-950/50 text-primary-300 border border-primary-700/50'
                  : 'bg-yellow-950/50 text-yellow-300 border border-yellow-700/50'
              }`}>
                {todo.is_complete ? (
                  <>
                    <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                    </svg>
                    Completed
                  </>
                ) : (
                  <>
                    <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
                    </svg>
                    Pending
                  </>
                )}
              </span>
            </div>
          </div>
        </div>
        <button
          onClick={handleDelete}
          className="flex-shrink-0 p-2 text-gray-600 hover:text-red-400 hover:bg-red-950/30 rounded-lg transition-all duration-200 group-hover:opacity-100 opacity-0 border border-transparent hover:border-red-500/30"
          title="Delete todo"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
        </button>
      </div>
    </div>
  );
}
