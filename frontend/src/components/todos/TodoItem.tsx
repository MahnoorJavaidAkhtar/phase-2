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
    <li className="px-6 py-4 hover:bg-gray-50">
      <div className="flex items-center justify-between">
        <div className="flex items-center flex-1">
          <input
            type="checkbox"
            checked={todo.is_complete}
            onChange={handleToggle}
            className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded cursor-pointer"
          />
          <div className="ml-3 flex-1">
            <p className={`text-sm font-medium ${todo.is_complete ? 'line-through text-gray-500' : 'text-gray-900'}`}>
              {todo.title}
            </p>
            {todo.description && (
              <p className="text-sm text-gray-500">{todo.description}</p>
            )}
          </div>
        </div>
        <div className="ml-4 flex items-center space-x-2">
          <button
            onClick={handleDelete}
            className="text-red-600 hover:text-red-800 text-sm font-medium"
          >
            Delete
          </button>
        </div>
      </div>
    </li>
  );
}
