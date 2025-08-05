#!/usr/bin/env python3
"""
Bug Fix Implementation

Critical bug fixes and improved error handling.
Fixed: 2025-08-05T18:57:58.751Z
"""

import logging
from typing import Optional, Union


class ErrorHandler:
    """Improved error handling and bug fixes"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.error_count = 0
    
    def safe_operation(self, data: Union[str, int, float]) -> Optional[str]:
        """Safely process data with proper error handling"""
        try:
            if data is None:
                raise ValueError("Input data cannot be None")
            
            # Fixed: Handle different data types properly
            if isinstance(data, (int, float)):
                result = f"numeric_result_{data * 2}"
            elif isinstance(data, str):
                result = f"string_result_{data.lower().strip()}"
            else:
                result = f"generic_result_{str(data)}"
            
            return result
            
        except ValueError as e:
            self.logger.error(f"ValueError in safe_operation: {e}")
            self.error_count += 1
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error in safe_operation: {e}")
            self.error_count += 1
            return None
    
    def validate_input(self, input_data: any) -> bool:
        """Validate input data with comprehensive checks"""
        try:
            # Fixed: More robust input validation
            if input_data is None:
                return False
            
            if isinstance(input_data, str) and len(input_data.strip()) == 0:
                return False
            
            if isinstance(input_data, (list, dict)) and len(input_data) == 0:
                return False
            
            return True
            
        except Exception:
            return False
    
    def get_error_stats(self) -> dict:
        """Return error statistics"""
        return {
            "total_errors": self.error_count,
            "timestamp": "2025-08-05T18:57:58.751Z"
        }


# Fixed: Improved main execution
if __name__ == "__main__":
    handler = ErrorHandler()
    
    # Test cases with various inputs
    test_cases = [None, "", "  ", "valid_string", 42, 3.14, [], {}]
    
    for test_case in test_cases:
        if handler.validate_input(test_case):
            result = handler.safe_operation(test_case)
            print(f"Input: {test_case} -> Result: {result}")
        else:
            print(f"Invalid input: {test_case}")
    
    print(f"Error statistics: {handler.get_error_stats()}")
