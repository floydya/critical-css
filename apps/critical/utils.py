
def generate_data_for_response(post_type, term_id, post_id, styles):
    return {
        'content': {
            'post_type': post_type,
            'term_id': term_id,
            'post_id': post_id,
            'styles': styles
        },
        'status': 200
    }
