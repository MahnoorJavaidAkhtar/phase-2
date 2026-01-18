/**
 * API client for backend communication.
 * Custom fetch-based client with authentication support.
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface RequestOptions extends RequestInit {
  token?: string;
}

/**
 * Make an authenticated API request.
 */
async function apiRequest<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<T> {
  const { token, ...fetchOptions } = options;

  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    ...fetchOptions.headers,
  };

  // Add Authorization header if token provided
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...fetchOptions,
    headers,
    credentials: 'include', // Include cookies for auth
  });

  // Handle non-2xx responses
  if (!response.ok) {
    const error = await response.json().catch(() => ({
      detail: 'An error occurred',
    }));
    throw new Error(error.detail || `HTTP ${response.status}`);
  }

  // Handle 204 No Content
  if (response.status === 204) {
    return {} as T;
  }

  return response.json();
}

/**
 * API client methods.
 */
export const apiClient = {
  /**
   * GET request.
   */
  get: <T>(endpoint: string, token?: string): Promise<T> =>
    apiRequest<T>(endpoint, { method: 'GET', token }),

  /**
   * POST request.
   */
  post: <T>(endpoint: string, data?: unknown, token?: string): Promise<T> =>
    apiRequest<T>(endpoint, {
      method: 'POST',
      body: data ? JSON.stringify(data) : undefined,
      token,
    }),

  /**
   * PUT request.
   */
  put: <T>(endpoint: string, data: unknown, token?: string): Promise<T> =>
    apiRequest<T>(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data),
      token,
    }),

  /**
   * PATCH request.
   */
  patch: <T>(endpoint: string, data: unknown, token?: string): Promise<T> =>
    apiRequest<T>(endpoint, {
      method: 'PATCH',
      body: JSON.stringify(data),
      token,
    }),

  /**
   * DELETE request.
   */
  delete: <T>(endpoint: string, token?: string): Promise<T> =>
    apiRequest<T>(endpoint, { method: 'DELETE', token }),
};
