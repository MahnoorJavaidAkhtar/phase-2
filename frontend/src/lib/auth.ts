/**
 * Authentication utilities for frontend.
 */

import { apiClient } from './api-client';
import { TokenResponse, User, SignupRequest, LoginRequest } from '@/types';

/**
 * Sign up a new user.
 */
export async function signup(email: string, password: string): Promise<{ message: string; user_id: number }> {
  const data: SignupRequest = { email, password };
  return apiClient.post('/auth/signup', data);
}

/**
 * Log in a user and store the token.
 */
export async function login(email: string, password: string): Promise<TokenResponse> {
  // OAuth2 form data format
  const formData = new URLSearchParams();
  formData.append('username', email); // OAuth2 uses 'username' field
  formData.append('password', password);

  const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'}/auth/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData,
    credentials: 'include', // Include cookies
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Login failed' }));
    throw new Error(error.detail || 'Login failed');
  }

  const tokenData: TokenResponse = await response.json();

  // Store token in localStorage for client-side access
  if (typeof window !== 'undefined') {
    localStorage.setItem('access_token', tokenData.access_token);
  }

  return tokenData;
}

/**
 * Log out the current user.
 */
export async function logout(): Promise<void> {
  const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;

  try {
    await apiClient.post('/auth/logout', undefined, token || undefined);
  } finally {
    // Clear token from localStorage regardless of API call success
    if (typeof window !== 'undefined') {
      localStorage.removeItem('access_token');
    }
  }
}

/**
 * Get the current authenticated user.
 */
export async function getCurrentUser(): Promise<User | null> {
  const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;

  if (!token) {
    return null;
  }

  try {
    return await apiClient.get<User>('/auth/me', token);
  } catch (error) {
    // Token is invalid or expired
    if (typeof window !== 'undefined') {
      localStorage.removeItem('access_token');
    }
    return null;
  }
}

/**
 * Check if user is authenticated.
 */
export function isAuthenticated(): boolean {
  if (typeof window === 'undefined') {
    return false;
  }
  return !!localStorage.getItem('access_token');
}
