"""Helper for creating a Redis client from environment variables."""

import os
import redis


def get_redis_client() -> redis.Redis:
    """
    Create a Redis client using `REDIS_HOST`, `REDIS_PORT` and `REDIS_PASSWORD` environment
    variables.  Defaults to `localhost:6379` with no password.
    """
    host = os.environ.get("REDIS_HOST", "localhost")
    port = int(os.environ.get("REDIS_PORT", 6379))
    password = os.environ.get("REDIS_PASSWORD") or None
    return redis.Redis(host=host, port=port, password=password, decode_responses=True)
