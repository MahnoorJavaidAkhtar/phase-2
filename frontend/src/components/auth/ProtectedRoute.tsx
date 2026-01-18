'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { isAuthenticated } from '@/lib/auth';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

/**
 * Protected route wrapper component.
 * Redirects to signin if user is not authenticated.
 */
export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const router = useRouter();

  useEffect(() => {
    if (!isAuthenticated()) {
      router.push('/signin');
    }
  }, [router]);

  // Show nothing while checking auth (prevents flash of protected content)
  if (!isAuthenticated()) {
    return null;
  }

  return <>{children}</>;
}
