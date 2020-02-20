CC = gcc
PWD := $(shell pwd)
CFLAGS = -fPIC -Wall -Wextra -O2 -g
LDFLAGS = -shared

RM = rm -f

CFLAGS += $(DFLAGS)


TARGET_LIB1 = matrix.so
TARGET_LIB2 = array.so
TARGET_LIB3 = operation.so
TARGET_LIBS = $(TARGET_LIB1) $(TARGET_LIB2) $(TARGET_LIB3)

SRCS1 = matrix.c
SRCS2 = array.c
SRCS3 = operation.c
SRCS = $(SRCS1) $(SRCS2) $(SRCS3) 

OBJS1 = $(SRCS1:.c=.o)
OBJS2 = $(SRCS2:.c=.o)
OBJS3 = $(SRCS3:.c=.o)
OBJS = $(OBJS1) $(OBJS2) $(OBJS3)


all: $(TARGET_LIBS)

$(TARGET_LIB1): $(OBJS1)
	$(CC) $(INC) $(LDFLAGS) $(CFLAGS) -o $@ $^

$(TARGET_LIB2): $(OBJS2)
	$(CC) $(INC) $(LDFLAGS) $(CFLAGS) -o $@ $^

$(TARGET_LIB3): $(OBJS3)
	$(CC) $(INC) $(LDFLAGS) $(CFLAGS) -o $@ $^

clean:
	$(RM) $(PWD)/*.so $(PWD)/*.o