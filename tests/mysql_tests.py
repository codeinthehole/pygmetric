import unittest
import mock

from pygmetric import mysql


STDOUT = """+-----------------------------------+---------------+
| Aborted_clients                   |         24473 |
| Aborted_connects                  |            82 |
| Binlog_cache_disk_use             |         75938 |
| Binlog_cache_use                  |      58687056 |
| Bytes_received                    | 1028745350408 |
| Bytes_sent                        | 3176259802173 |
| Com_admin_commands                |    2152370079 |
| Com_assign_to_keycache            |             0 |
| Com_alter_db                      |             0 |
| Com_alter_db_upgrade              |             0 |
| Com_alter_event                   |             0 |
| Com_alter_function                |             0 |
| Com_alter_procedure               |             0 |
| Com_alter_server                  |             0 |
| Com_alter_table                   |             1 |
| Com_alter_tablespace              |             0 |
| Com_analyze                       |             0 |
| Com_backup_table                  |             0 |
| Com_begin                         |             0 |
| Com_binlog                        |             0 |
| Com_call_procedure                |             0 |
| Com_change_db                     |            17 |
| Com_change_master                 |             0 |
| Com_check                         |             0 |
| Com_checksum                      |             0 |
| Com_commit                        |     176495692 |
| Com_create_db                     |             0 |
| Com_create_event                  |             0 |
| Com_create_function               |             0 |
| Com_create_index                  |             4 |
| Com_create_procedure              |             0 |
| Com_create_server                 |             0 |
| Com_create_table                  |             1 |
| Com_create_trigger                |             0 |
| Com_create_udf                    |             0 |
| Com_create_user                   |             0 |
| Com_create_view                   |             0 |
| Com_dealloc_sql                   |             0 |
| Com_delete                        |        872745 |
| Com_delete_multi                  |             0 |
| Com_do                            |             0 |
| Com_drop_db                       |             0 |
| Com_drop_event                    |             0 |
| Com_drop_function                 |             0 |
| Com_drop_index                    |             0 |
| Com_drop_procedure                |             0 |
| Com_drop_server                   |             0 |
| Com_drop_table                    |             0 |
| Com_drop_trigger                  |             0 |
| Com_drop_user                     |             0 |
| Com_drop_view                     |             0 |
| Com_empty_query                   |             0 |
| Com_execute_sql                   |             0 |
| Com_flush                         |            35 |
| Com_grant                         |             0 |
| Com_ha_close                      |             0 |
| Com_ha_open                       |             0 |
| Com_ha_read                       |             0 |
| Com_help                          |             0 |
| Com_insert                        |      11003204 |
| Com_insert_select                 |             0 |
| Com_install_plugin                |             0 |
| Com_kill                          |             2 |
| Com_load                          |        266282 |
| Com_load_master_data              |             0 |
| Com_load_master_table             |             0 |
| Com_lock_tables                   |             0 |
| Com_optimize                      |             0 |
| Com_preload_keys                  |             0 |
| Com_prepare_sql                   |             0 |
| Com_purge                         |             0 |
| Com_purge_before_date             |             0 |
| Com_release_savepoint             |        606996 |
| Com_rename_table                  |             0 |
| Com_rename_user                   |             0 |
| Com_repair                        |             0 |
| Com_replace                       |             0 |
| Com_replace_select                |             0 |
| Com_reset                         |             0 |
| Com_restore_table                 |             0 |
| Com_revoke                        |             0 |
| Com_revoke_all                    |             0 |
| Com_rollback                      |         40464 |
| Com_rollback_to_savepoint         |          2769 |
| Com_savepoint                     |      15556478 |
| Com_select                        |     894856486 |
| Com_set_option                    |      62692570 |
| Com_show_authors                  |             0 |
| Com_show_binlog_events            |             0 |
| Com_show_binlogs                  |         10030 |
| Com_show_charsets                 |             0 |
| Com_show_collations               |             0 |
| Com_show_column_types             |             0 |
| Com_show_contributors             |             0 |
| Com_show_create_db                |             0 |
| Com_show_create_event             |             0 |
| Com_show_create_func              |             0 |
| Com_show_create_proc              |             0 |
| Com_show_create_table             |            58 |
| Com_show_create_trigger           |             0 |
| Com_show_databases                |            51 |
| Com_show_engine_logs              |             0 |
| Com_show_engine_mutex             |             0 |
| Com_show_engine_status            |         10946 |
| Com_show_events                   |             0 |
| Com_show_errors                   |             0 |
| Com_show_fields                   |          9198 |
| Com_show_function_status          |             0 |
| Com_show_grants                   |             0 |
| Com_show_keys                     |            14 |
| Com_show_master_status            |             2 |
| Com_show_new_master               |             0 |
| Com_show_open_tables              |             0 |
| Com_show_plugins                  |             0 |
| Com_show_privileges               |             0 |
| Com_show_procedure_status         |             0 |
| Com_show_processlist              |           241 |
| Com_show_profile                  |             0 |
| Com_show_profiles                 |             0 |
| Com_show_slave_hosts              |             0 |
| Com_show_slave_status             |         10023 |
| Com_show_status                   |         58302 |
| Com_show_storage_engines          |             0 |
| Com_show_table_status             |            56 |
| Com_show_tables                   |            58 |
| Com_show_triggers                 |             0 |
| Com_show_variables                |         11002 |
| Com_show_warnings                 |            55 |
| Com_slave_start                   |             0 |
| Com_slave_stop                    |             0 |
| Com_stmt_close                    |             0 |
| Com_stmt_execute                  |             0 |
| Com_stmt_fetch                    |             0 |
| Com_stmt_prepare                  |             0 |
| Com_stmt_reprepare                |             0 |
| Com_stmt_reset                    |             0 |
| Com_stmt_send_long_data           |             0 |
| Com_truncate                      |             0 |
| Com_uninstall_plugin              |             0 |
| Com_unlock_tables                 |             0 |
| Com_update                        |     152365778 |
| Com_update_multi                  |             0 |
| Com_xa_commit                     |             0 |
| Com_xa_end                        |             0 |
| Com_xa_prepare                    |             0 |
| Com_xa_recover                    |             0 |
| Com_xa_rollback                   |             0 |
| Com_xa_start                      |             0 |
| Compression                       |           OFF |
| Connections                       |      17691201 |
| Created_tmp_disk_tables           |       6717413 |
| Created_tmp_files                 |         65863 |
| Created_tmp_tables                |      10122367 |
| Delayed_errors                    |             0 |
| Delayed_insert_threads            |             0 |
| Delayed_writes                    |             0 |
| Flush_commands                    |             1 |
| Handler_commit                    |    1355062554 |
| Handler_delete                    |      92281479 |
| Handler_discover                  |             0 |
| Handler_prepare                   |     238315960 |
| Handler_read_first                |      13737350 |
| Handler_read_key                  |    5510384504 |
| Handler_read_next                 |  777739791735 |
| Handler_read_prev                 |     269264307 |
| Handler_read_rnd                  |     259099631 |
| Handler_read_rnd_next             | 1574207601568 |
| Handler_rollback                  |        388151 |
| Handler_savepoint                 |       9695864 |
| Handler_savepoint_rollback        |          2769 |
| Handler_update                    |     165655218 |
| Handler_write                     |     172316650 |
| Innodb_buffer_pool_pages_data     |        377286 |
| Innodb_buffer_pool_pages_dirty    |          2573 |
| Innodb_buffer_pool_pages_flushed  |      90612660 |
| Innodb_buffer_pool_pages_free     |             2 |
| Innodb_buffer_pool_pages_misc     |         15928 |
| Innodb_buffer_pool_pages_total    |        393216 |
| Innodb_buffer_pool_read_ahead_rnd |       1567483 |
| Innodb_buffer_pool_read_ahead_seq |        825008 |
| Innodb_buffer_pool_read_requests  |  739476600066 |
| Innodb_buffer_pool_reads          |     103962801 |
| Innodb_buffer_pool_wait_free      |             0 |
| Innodb_buffer_pool_write_requests |    3353944439 |
| Innodb_data_fsyncs                |       6497162 |
| Innodb_data_pending_fsyncs        |             1 |
| Innodb_data_pending_reads         |             0 |
| Innodb_data_pending_writes        |             0 |
| Innodb_data_read                  | 3079891750912 |
| Innodb_data_reads                 |     123682976 |
| Innodb_data_writes                |     297951623 |
| Innodb_data_written               | 3249276207616 |
| Innodb_dblwr_pages_written        |      90612788 |
| Innodb_dblwr_writes               |       1338028 |
| Innodb_log_waits                  |          3367 |
| Innodb_log_write_requests         |     366261719 |
| Innodb_log_writes                 |     224235779 |
| Innodb_os_log_fsyncs              |       3822255 |
| Innodb_os_log_pending_fsyncs      |             0 |
| Innodb_os_log_pending_writes      |             0 |
| Innodb_os_log_written             |  279872190976 |
| Innodb_page_size                  |         16384 |
| Innodb_pages_created              |       3612634 |
| Innodb_pages_read                 |     187981046 |
| Innodb_pages_written              |      90612788 |
| Innodb_row_lock_current_waits     |             0 |
| Innodb_row_lock_time              |     440567084 |
| Innodb_row_lock_time_avg          |          2077 |
| Innodb_row_lock_time_max          |        330631 |
| Innodb_row_lock_waits             |        212095 |
| Innodb_rows_deleted               |      92281457 |
| Innodb_rows_inserted              |     118011078 |
| Innodb_rows_read                  | 2349244437117 |
| Innodb_rows_updated               |     163641219 |
| Key_blocks_not_flushed            |             0 |
| Key_blocks_unused                 |         13396 |
| Key_blocks_used                   |          2220 |
| Key_read_requests                 |      33263586 |
| Key_reads                         |             3 |
| Key_write_requests                |       5293445 |
| Key_writes                        |             0 |
| Last_query_cost                   |      0.000000 |
| Max_used_connections              |           301 |
| Not_flushed_delayed_rows          |             0 |
| Open_files                        |             4 |
| Open_streams                      |             0 |
| Open_table_definitions            |           210 |
| Open_tables                       |            64 |
| Opened_files                      |      28736956 |
| Opened_table_definitions          |           225 |
| Opened_tables                     |      11535472 |
| Prepared_stmt_count               |             0 |
| Qcache_free_blocks                |           863 |
| Qcache_free_memory                |       6111120 |
| Qcache_hits                       |    1079435027 |
| Qcache_inserts                    |     500404683 |
| Qcache_lowmem_prunes              |     320043363 |
| Qcache_not_cached                 |     394613750 |
| Qcache_queries_in_cache           |          6987 |
| Qcache_total_blocks               |         14878 |
| Queries                           |    2411941540 |
| Questions                         |    2411941540 |
| Rpl_status                        |          NULL |
| Select_full_join                  |            56 |
| Select_full_range_join            |             0 |
| Select_range                      |      23096318 |
| Select_range_check                |             0 |
| Select_scan                       |      13775608 |
| Slave_open_temp_tables            |             0 |
| Slave_retried_transactions        |             0 |
| Slave_running                     |           OFF |
| Slow_launch_threads               |             0 |
| Slow_queries                      |        204648 |
| Sort_merge_passes                 |        395205 |
| Sort_range                        |      21797651 |
| Sort_rows                         |    1007504249 |
| Sort_scan                         |      12725760 |
| Ssl_accept_renegotiates           |             0 |
| Ssl_accepts                       |             0 |
| Ssl_callback_cache_hits           |             0 |
| Ssl_cipher                        |               |
| Ssl_cipher_list                   |               |
| Ssl_client_connects               |             0 |
| Ssl_connect_renegotiates          |             0 |
| Ssl_ctx_verify_depth              |             0 |
| Ssl_ctx_verify_mode               |             0 |
| Ssl_default_timeout               |             0 |
| Ssl_finished_accepts              |             0 |
| Ssl_finished_connects             |             0 |
| Ssl_session_cache_hits            |             0 |
| Ssl_session_cache_misses          |             0 |
| Ssl_session_cache_mode            |          NONE |
| Ssl_session_cache_overflows       |             0 |
| Ssl_session_cache_size            |             0 |
| Ssl_session_cache_timeouts        |             0 |
| Ssl_sessions_reused               |             0 |
| Ssl_used_session_cache_entries    |             0 |
| Ssl_verify_depth                  |             0 |
| Ssl_verify_mode                   |             0 |
| Ssl_version                       |               |
| Table_locks_immediate             |    1284767674 |
| Table_locks_waited                |             3 |
| Tc_log_max_pages_used             |             0 |
| Tc_log_page_size                  |             0 |
| Tc_log_page_waits                 |             9 |
| Threads_cached                    |             3 |
| Threads_connected                 |            15 |
| Threads_created                   |        371342 |
| Threads_running                   |             3 |
| Uptime                            |       3036021 |
| Uptime_since_flush_status         |       3036021 |
+-----------------------------------+---------------+"""


@mock.patch('pygmetric.shell.run')
class MySQLTests(unittest.TestCase):

    def test_threads_connected(self, mock_run):
        mock_run.return_value = STDOUT
        stats = mysql.fetch_stats(user='ganglia', password='cheese')
        self.assertEqual(stats['mysql_threads_connected']['value'], 15)

    @mock.patch('pygmetric.get_rate')
    def test_connections_rate_captured(self, mock_rate, mock_run):
        mock_run.return_value = STDOUT
        mock_rate.return_value = 3
        stats = mysql.fetch_stats(user='ganglia', password='cheese')
        self.assertEqual(stats['mysql_connections_rate']['value'], 3)
