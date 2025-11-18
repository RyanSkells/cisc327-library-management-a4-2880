"""
Search Routes - Book search functionality
"""

from flask import Blueprint, render_template, request, flash
from services.library_service import get_patron_status_report
record_bp = Blueprint('record', __name__)


@record_bp.route('/record')
def user_records():
    """
    Implement R7
    """
    patron_id = request.args.get('q', '').strip()
    if not patron_id or len(str(patron_id)) != 6:
        flash("invalid/missing patron ID ", 'error')
        return render_template('user_records.html', records=[], patron_id=patron_id, total_fee=[],
                           borrowed_books=[], borrowed_count=[])

    borrowed_books, total_fee, borrowed_count, records = get_patron_status_report(patron_id)

    if not records:
        flash("No records for user", 'error')
        return render_template('user_records.html', records=[])

    return render_template('user_records.html', records=records, patron_id=patron_id, total_fee=total_fee,
                           borrowed_books=borrowed_books, borrowed_count=borrowed_count)

