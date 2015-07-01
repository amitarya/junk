LDFLAGS =
CXX = clang++
SRCDIR = src
OBJDIR = build

CXXFLAGS := -I./include --std=c++0x
DFLAGS :=
OBJECTS :=
include $(SRCDIR)/Makefile.mk

imageConverter: $(OBJECTS)
	@echo [LD] $@
	@$(CXX) $(DFLAGS) -o $@ $^

clean:
	@rm -rf $(OBJDIR)
	@rm imageConverter

