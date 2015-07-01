SRCS := tlvObjects.cpp \
		 interpretter.cpp \
		 pixMap.cpp \
		 main.cpp

OBJECTS := $(patsubst %.cpp, $(OBJDIR)/%.o, $(SRCS))

$(OBJDIR)/%.o: $(SRCDIR)/%.cpp $(wildcard $(INCDIR)/*.h)
	@mkdir -p $(dir $@)
	@echo [CXX] $@
	@$(CXX) $(DFLAGS) -c $(CXXFLAGS) -o $@ $<
