bins_main : bins_setup bin_intro print_bins bins_worker
bins_setup: bin_dirs libs
	@date>>"$(LOG_PATH)main_build.log"
bin_intro :
	@echo "$(CYAN)$(BOLD)BINARIES$(RESET)"
	
bins_logs:
	@echo "$(YELLOW)$(LOG_PATH)main_build.log$(REST)"
bins_close: bins_logs
	@echo "$(GREEN)Done$(RESET)" $(DONE)
bins_worker_intro:
	@echo Compiling Sources
bins_worker: bins_worker_intro $(MAIN_BIN)
print_bins:
	@echo Expected Targets
	@ for item in $(MAIN_BIN); do \
		echo '-' $$item;\
	done
# $(MAIN_BIN)