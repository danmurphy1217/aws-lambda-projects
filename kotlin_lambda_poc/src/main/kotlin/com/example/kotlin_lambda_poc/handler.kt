package com.example.kotlin_lambda_poc;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

class Handler: RequestHandler<Map<String, String>, String> {
    override fun handleRequest(event: Map<String, String>, context: Context): String {
        return "hello world!"
    }
}

