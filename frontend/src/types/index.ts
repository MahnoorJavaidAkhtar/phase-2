/**
 * TypeScript type definitions for API entities.
 */

/**
 * User entity.
 */
export interface User {
  id: number;
  email: string;
  created_at: string;
}

/**
 * Todo entity.
 */
export interface Todo {
  id: number;
  user_id: number;
  title: string;
  description: string | null;
  is_complete: boolean;
  created_at: string;
  updated_at: string;
}

/**
 * Todo creation payload.
 */
export interface TodoCreate {
  title: string;
  description?: string | null;
}

/**
 * Todo update payload.
 */
export interface TodoUpdate {
  title: string;
  description?: string | null;
  is_complete?: boolean;
}

/**
 * Authentication token response.
 */
export interface TokenResponse {
  access_token: string;
  token_type: string;
  expires_in: number;
}

/**
 * User signup payload.
 */
export interface SignupRequest {
  email: string;
  password: string;
}

/**
 * User login payload.
 */
export interface LoginRequest {
  username: string; // email
  password: string;
}

/**
 * API error response.
 */
export interface ApiError {
  detail: string;
}
